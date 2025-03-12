import { LoaderFunctionArgs } from "@remix-run/node"
import { redirect } from "@remix-run/node"

export function requireAuth({request}:LoaderFunctionArgs) {
  const cookie = request.headers.get("Cookie")
  const token = cookie?.match(/token=([^;]+)/)?.[1]

  if (!token) {
    throw redirect("/?error=unauthorized")
  }

  return token
}

