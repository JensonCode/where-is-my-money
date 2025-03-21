import { LoginFormData, LoginResponse } from "../types/login";
import { getValidationErrors } from "../lib/api-error";
import { createUserSession } from "../utils/auth";

const API_URL = process.env.API_BASE_URL + "/users/login";

export async function loginAction(formData: LoginFormData) {
  try {
    const requestBody = new FormData();

    requestBody.append("username", formData.username);
    requestBody.append("password", formData.password);

    const response = await fetch(API_URL, {
      method: "POST",
      body: requestBody,
    });

    if (response.status === 422) {
      const error = await response.json();
      const formErrors = getValidationErrors(error);

      return {
        errors: { form: JSON.stringify(formErrors) },
        success: false,
        formName: "login",
      };
    }

    if (!response.ok) {
      return {
        errors: { form: "Invalid credentials" },
        success: false,
        formName: "login",
      };
    }

    const loginResponse = (await response.json()) as LoginResponse;

    return createUserSession(loginResponse.access_token, "/admin");
  } catch (error) {
    return {
      errors: { form: "Failed to login. Please try again." },
      success: false,
      formName: "login",
    };
  }
}
