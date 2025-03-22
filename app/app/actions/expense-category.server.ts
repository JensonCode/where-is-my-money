import type { ExpenseCategoryFormData, ExpenseCategoryResponse } from '../types/expense-category';
import { getValidationErrors } from '../lib/api-error';

const API_URL = process.env.API_BASE_URL + '/expense-categories';

export async function getExpenseCategoriesAction(token: string) {
  try {
    const response = await fetch(API_URL, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (response.status === 422) {
      const error = await response.json();
      const formErrors = getValidationErrors(error);

      return {
        errors: { message: JSON.stringify(formErrors) },
        success: false,
      };
    }

    if (!response.ok) {
      return {
        errors: { message: 'Internal Server Error' },
        success: false,
      };
    }

    const expenseCategoryResponse =
      (await response.json()) as ExpenseCategoryResponse[];

    return {
      data: expenseCategoryResponse,
      success: true,
    };
  } catch (error) {
    return {
      errors: { message: 'Failed to get expense catrgories.' },
      success: false,
    };
  }
}

export async function createExpenseCategoryAction(token: string, formData: ExpenseCategoryFormData) {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });

    if (response.status === 422) {
      const error = await response.json();
      const formErrors = getValidationErrors(error);

      return {
        errors: { message: JSON.stringify(formErrors) },
        success: false,
      };
    }

    if (!response.ok) {
      return {
        errors: { message: 'Failed to create expense category.' },
        success: false,
      };
    }

    const expenseCategoryResponse =
      (await response.json()) as ExpenseCategoryResponse;

    return {
      data: expenseCategoryResponse,
      success: true,
    };
  } catch (error) {
    return {
      errors: { message: 'Failed to create expense category.' },
      success: false,
    };
  }
}

export async function updateExpenseCategoryAction(
  token: string,
  id: string,
  name: string
) {
  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: 'PUT',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name }),
    });

    if (!response.ok) {
      return {
        errors: { message: 'Failed to update expense category.' },
        success: false,
      };
    }

    const expenseCategoryResponse =
      (await response.json()) as ExpenseCategoryResponse;

    return {
      data: expenseCategoryResponse,
      success: true,
    };
  } catch (error) {
    return {
      errors: { message: 'Failed to update expense category.' },
      success: false,
    };
  }
}

export async function deleteExpenseCategoryAction(token: string, id: string) {
  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: 'DELETE',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      return {
        errors: { message: 'Failed to delete expense category.' },
        success: false,
      };
    }

    return {
      success: true,
    };
  } catch (error) {
    return {
      errors: { message: 'Failed to delete expense category.' },
      success: false,
    };
  }
}
