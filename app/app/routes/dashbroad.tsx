import { getUserToken } from '../utils/auth';
import { LoaderFunctionArgs } from '@remix-run/node';

export async function loader({ request }: LoaderFunctionArgs) {
  const token = await getUserToken(request);

  return Response.json({ token });
}

export default function Dashbroad() {

  return <div>Dashbroad</div>;
}
