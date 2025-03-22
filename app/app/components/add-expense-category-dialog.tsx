import { Form, useActionData, useNavigation } from "@remix-run/react";
import { Loader2 } from "lucide-react";

import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { Label } from "./ui/label";
import { Icon, iconList, IconName } from "./icon";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./ui/dialog";
import { action } from "../routes/admin";
import { useEffect, useState } from "react";

export default function AddExpenseCategoryDialog() {
  const actionData = useActionData<typeof action>();
  const [showSuccess, setShowSuccess] = useState(false);

  useEffect(() => {
    if (
      actionData?.success &&
      actionData.formName === "create-expense-category"
    ) {
      setShowSuccess(true);
    }
  }, [actionData]);

  return (
    <Dialog onOpenChange={() => setShowSuccess(false)}>
      <DialogTrigger className="mb-4 text-xl font-bold">
        Add Expense Category
      </DialogTrigger>

      {showSuccess ? (
        <DialogContent>
          <div className="flex flex-col items-center gap-4 pt-4">
            <p className="font-medium text-green-600">
              Category created successfully!
            </p>
            <DialogClose asChild>
              <Button variant="secondary">Close</Button>
            </DialogClose>
          </div>
        </DialogContent>
      ) : (
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Add Expense Category</DialogTitle>
            <DialogDescription>
              Add a new category to group your expenses
            </DialogDescription>
          </DialogHeader>

          <CreateExpenseCategoryForm />
        </DialogContent>
      )}
    </Dialog>
  );
}

function CreateExpenseCategoryForm() {
  const navigation = useNavigation();

  const [selectedIcon, setSelectedIcon] = useState<IconName | "dummy-icon">(
    "dummy-icon",
  );

  return (
    <Form method="post" className="flex flex-col gap-4">
      <div className="mb-4">
        <Label htmlFor="icon">Icon</Label>
        <input type="hidden" name="icon" value={selectedIcon} />
        <div className="flex flex-wrap gap-2">
          {iconList.map((icon, index) => (
            <Button
              type="button"
              variant={selectedIcon === icon ? "default" : "outline"}
              size="icon"
              key={index}
              onClick={() => setSelectedIcon(icon)}
            >
              <Icon icon={icon} />
            </Button>
          ))}
        </div>
      </div>

      <div className="mb-4">
        <Label htmlFor="name">New Category</Label>
        <Input
          id="name"
          name="name"
          type="text"
          required
          placeholder='"Groceries"'
        />
      </div>

      <Button
        type="submit"
        name="_action"
        value="create-expense-category"
        disabled={navigation.state === "submitting"}
      >
        {navigation.state === "submitting" ? (
          <Loader2 className="size-4 animate-spin" />
        ) : (
          "Create"
        )}
      </Button>
    </Form>
  );
}
