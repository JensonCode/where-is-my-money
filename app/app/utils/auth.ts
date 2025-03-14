import { createCookieSessionStorage, redirect } from '@remix-run/node';

const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: '__session',
    secrets: [process.env.SESSION_SECRET!],
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 24 * 30,
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
  },
});

export async function getUserSession(request: Request) {
  return await sessionStorage.getSession(request.headers.get('Cookie'));
}

export async function getUserToken(request: Request) {
  const session = await getUserSession(request);
  const token = session.get('token');
  return token;
}

export async function requireAuth(request: Request) {
  const token = await getUserToken(request);

  if (!token) {
    throw redirect('/');
  }

  return token;
}

export async function createUserSession(token: string, redirectTo: string) {
  const session = await sessionStorage.getSession();
  session.set('token', token);

  return redirect(redirectTo, {
    headers: { 'Set-Cookie': await sessionStorage.commitSession(session) },
  });
}

export async function logout(request: Request) {
  const session = await sessionStorage.getSession(
    request.headers.get('Cookie')
  );

  return redirect('/', {
    headers: {
      'Set-Cookie': await sessionStorage.destroySession(session),
    },
  });
}
