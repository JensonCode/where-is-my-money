import { components } from '../types/api';

// fastapi ValidationError
type ValidationError = components['schemas']['HTTPValidationError'];

export const getValidationErrors = (error: ValidationError) => {
  const formErrors: Record<string, string> = {};

  error.detail?.forEach((error) => {
    const field = error.loc[1] as string;
    const message = error.msg;
    formErrors[field] = message;
  });

  return formErrors;
};
