import { Fragment } from "react/jsx-runtime";
import { Outlet, redirect } from "@remix-run/react";
import { LoaderFunctionArgs } from "@remix-run/node";

import { getUserToken } from "../utils/auth";
import { createExpenseCategoryAction, getExpenseCategoriesAction } from "../actions/expense-category.server";
import Nav from "../components/nav";
import { ActionFunctionArgs } from "@remix-run/node";
import { ExpenseCategoryFormData } from "~/types/expense-category";

const actionTags = ["create-expense-category"] as const;
type ACTION_TAG = typeof actionTags[number];

export async function action({ request }: ActionFunctionArgs) {
  const token = await getUserToken(request);

  const actionReqest = Object.fromEntries(await request.formData());

  const tag = actionReqest._action as ACTION_TAG
  switch (tag) {
    case "create-expense-category": {
      const data: ExpenseCategoryFormData = {
        name: actionReqest.name.toString()
      }
      return await createExpenseCategoryAction(
        token,
        data
      );
    }
    default:
      return null
  }
}

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
