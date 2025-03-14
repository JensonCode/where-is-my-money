import { requireAuth } from '../utils/auth';
import { useLoaderData } from '@remix-run/react';
import { LoaderFunctionArgs } from '@remix-run/node';

export async function loader({ request }: LoaderFunctionArgs) {
  const token = await requireAuth(request);

  return Response.json({ token });
}

export default function Dashbroad() {
  const { token } = useLoaderData<typeof loader>();
  console.log(token);
  return <div>Dashbroad</div>;
}
