import { Form, useLoaderData } from "@remix-run/react";

import { AdminLayoutLoader } from "../routes/admin";

import {
  Drawer,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "./ui/drawer";
import { Button } from "./ui/button";

import { SquarePlus } from "lucide-react";

export default function AddExpenseDrawer() {
  return (
    <Drawer>
      <DrawerTrigger asChild>
        <Button>
          <SquarePlus />
          <span>Add Expense Record</span>
        </Button>
      </DrawerTrigger>

      <DrawerContent>
        <div className="mx-auto w-full max-w-sm">
          <DrawerHeader>
            <DrawerTitle>Add an Expense Record</DrawerTitle>
            <DrawerDescription>
              Select category and enter amount. Shortcuts will autofill the
              description!
            </DrawerDescription>
          </DrawerHeader>
          <div className="p-4 pb-0">
            <CreateExpenseForm />
          </div>
          <DrawerFooter>
            <Button type="submit" form="create-expense-form">
              Submit
            </Button>
          </DrawerFooter>
        </div>
      </DrawerContent>
    </Drawer>
  );
}

function CreateExpenseForm() {
  const { expenseCategories } = useLoaderData<AdminLayoutLoader>();

  return (
    <Form id="create-expense-form" method="post">
      <div>
        <label htmlFor="category">Category</label>

        {expenseCategories?.map((category) => (
          <div key={category.id}>{category.name}</div>
        ))}
      </div>
    </Form>
  );
}
