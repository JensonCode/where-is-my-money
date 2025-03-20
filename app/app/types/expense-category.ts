import type { components } from './api';

export type ExpenseCategory = components['schemas']['ExpenseCategoryBase'];

export type ExpenseCategoryFormData =
  components['schemas']['ExpenseCategoryRequest'];
export type ExpenseCategoryResponse =
  components['schemas']['ExpenseCategoryResponse'];
