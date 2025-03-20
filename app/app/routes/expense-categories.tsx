import { useLoaderData } from '@remix-run/react';
import { LoaderFunctionArgs } from '@remix-run/node';
import { getExpenseCategoriesAction } from '../actions/expense-category.server';

import { getUserToken } from '../utils/auth';

import { Badge } from '../components/ui/badge';

export async function loader({ request }: LoaderFunctionArgs) {
  const token = await getUserToken(request);
  const { data, errors, success } = await getExpenseCategoriesAction(token);
  return { data, errors, success };
}

export default function ExpenseCategories() {
  const { data, errors, success } = useLoaderData<typeof loader>();

  if (!success && !!errors) {
    return <div>Error: {errors.message}</div>;
  }

  if (!data) {
    return <div>No data</div>;
  }

  return (
    <div>
      {data.map((category) => (
        <Badge key={category.id}>{category.name}</Badge>
      ))}
    </div>
  );
}
