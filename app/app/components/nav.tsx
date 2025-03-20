import { Menu, SquarePlus } from "lucide-react";
import { Button } from "./ui/button";
import {
    Sheet,
    SheetContent,
    SheetTrigger,
} from "./ui/sheet"
import {
    Drawer,
    DrawerClose,
    DrawerContent,
    DrawerDescription,
    DrawerFooter,
    DrawerHeader,
    DrawerTitle,
    DrawerTrigger,
} from "./ui/drawer"
import CreateExpenseCategoryForm from "./create-expense-category-form";

export default function Nav() {
    return (
        <header>
            <nav>
                <ul className="h-[60px] border-b flex items-center justify-end gap-4 px-4">
                    <li>
                        <AddExpenseDrawer />
                    </li>
                    <li>
                        <NavMenu />
                    </li>
                </ul>
            </nav>
        </header>
    )
}

const NavMenu = () => {
    return (
        <Sheet>
            <SheetTrigger>
                <Menu />
            </SheetTrigger>
            <SheetContent className="py-10">
                <AddExpenseDrawer />
                <nav>
                    <ul className="h-full flex flex-col items-start gap-4 p-4">
                        <li>
                            Check every Expense Record
                        </li>
                        <li>
                            <span>
                                Manage Expense Categories
                            </span>
                        </li>
                        <li>
                            <span>
                                Manage Shortcuts
                            </span>
                        </li>
                    </ul>
                </nav>
            </SheetContent>
        </Sheet>
    )
}

const AddExpenseDrawer = () => {
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
                        <DrawerDescription>Select category and enter amount. Shortcuts will autofill the description!</DrawerDescription>
                    </DrawerHeader>
                    <div className="p-4 pb-0">
                        Form goes here
                    </div>
                    <DrawerFooter>
                        <Button>Submit</Button>
                        <DrawerClose asChild>
                            <Button variant="outline">Cancel</Button>
                        </DrawerClose>
                    </DrawerFooter>
                </div>
            </DrawerContent>
        </Drawer>
    )
}