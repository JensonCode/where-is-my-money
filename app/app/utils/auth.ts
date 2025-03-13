import { redirect } from '@remix-run/node';

export function requireAuth(request: Request) {
  const cookie = request.headers.get('Cookie');
  const token = cookie?.match(/token=([^;]+)/)?.[1];

  if (!token) {
    throw redirect('/');
  }

  return token;
}
