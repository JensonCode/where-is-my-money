import { Fragment } from "react/jsx-runtime";
import { Outlet, redirect } from "@remix-run/react";
import { LoaderFunctionArgs } from "@remix-run/node";

import { getUserToken } from "../utils/auth";
import { getExpenseCategoriesAction } from "../actions/expense-category.server";
import Nav from "../components/nav";

export async function loader({ request }: LoaderFunctionArgs) {
  const token = await getUserToken(request);
  if (!token) {
    throw redirect("/");
  }

  const expenseCategoriesResponse = await getExpenseCategoriesAction(token);
  if (!expenseCategoriesResponse.success) {
    throw new Error("Failed to fetch expense categories");
  }

  return { expenseCategories: expenseCategoriesResponse.data };
}

export type AdminLayoutLoader = typeof loader;

export default function AdminLayout() {
  return (
    <Fragment>
      <Nav />
      <Outlet />
    </Fragment>
  );
}
