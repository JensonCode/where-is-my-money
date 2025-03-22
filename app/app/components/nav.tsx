import { Sheet, SheetContent, SheetTrigger } from "./ui/sheet";

import AddExpenseDrawer from "./add-expense-drawer";
import AddExpenseCategoryDialog from "./add-expense-category-dialog";

import { Menu } from "lucide-react";

export default function Nav() {
  return (
    <header>
      <nav>
        <ul className="flex h-[60px] items-center justify-end gap-4 border-b px-4">
          <li>
            <AddExpenseDrawer />
          </li>
          <li>
            <Sheet>
              <SheetTrigger>
                <Menu />
              </SheetTrigger>
              <SheetContent className="py-10">
                <AddExpenseDrawer />

                <nav className="flex h-full flex-col items-start gap-4 p-4">
                  <NavGroup>
                    <li>
                      <span>Check every Expense Record</span>
                    </li>
                  </NavGroup>
                  <NavGroup>
                    <li>
                      <span>Manage Expense Categories</span>
                    </li>
                    <li>
                      <AddExpenseCategoryDialog />
                    </li>
                  </NavGroup>
                  <NavGroup>
                    <li>
                      <span>Manage Shortcuts</span>
                    </li>
                  </NavGroup>
                </nav>
              </SheetContent>
            </Sheet>
          </li>
        </ul>
      </nav>
    </header>
  );
}

const NavGroup = ({ children }: { children: React.ReactNode }) => {
  return (
    <ul className="flex h-full flex-col items-start gap-4 p-4">{children}</ul>
  );
};
