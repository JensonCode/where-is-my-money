import { Form, useNavigation } from '@remix-run/react';
import { Loader2 } from 'lucide-react';

import { Input } from './ui/input';
import { Button } from './ui/button';
import { Label } from './ui/label';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "./ui/dialog"

export default function AddExpenseCategoryDialog() {
    return (
        <Dialog>
            <DialogTrigger className="text-xl font-bold mb-4">Add Expense Category</DialogTrigger>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Add Expense Category</DialogTitle>
                    <DialogDescription>
                        Add a new category to group your expenses
                    </DialogDescription>
                </DialogHeader>

                <CreateExpenseCategoryForm />
            </DialogContent>
        </Dialog>

    );
}


function CreateExpenseCategoryForm() {
    const navigation = useNavigation();

    return (
        <Form method='post'>
            <div className='mb-4'>
                <Label htmlFor='name'>New Category</Label>
                <Input
                    id='name'
                    name='name'
                    type='text'
                    required
                    placeholder='"Groceries"'
                />
            </div>

            <Button
                type='submit'
                name='_action'
                value="create-expense-category"
                disabled={navigation.state === 'submitting'}
            >
                {navigation.state === 'submitting' ? (
                    <Loader2 className='size-4 animate-spin' />
                ) : (
                    'Create'
                )}
            </Button>
        </Form>
    );
}
