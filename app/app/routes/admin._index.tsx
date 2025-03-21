import { getUserToken } from "../utils/auth";
import { LoaderFunctionArgs } from "@remix-run/node";

//import { useLoaderData } from "@remix-run/react";
export async function loader({ request }: LoaderFunctionArgs) {
  const token = await getUserToken(request);

  return Response.json({ token });
}

export default function Dashbroad() {
  //const { token } = useLoaderData<typeof loader>();

  return <div>Admin Index</div>;
}
