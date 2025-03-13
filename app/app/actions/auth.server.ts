import type { components } from "~/types/api"

type LoginFormData = components["schemas"]["Body_login_users_login_post"]
type LoginResponse = components["schemas"]["LoginResponse"]
type ValidationError = components["schemas"]["HTTPValidationError"]

const API_URL = process.env.API_BASE_URL + "/users/login"

export async function loginAction(formData: LoginFormData) {
    try {
        const formBody = new URLSearchParams()

        Object.entries(formData).forEach(([key, value]) => {
            if (value !== null) {
                formBody.append(key, value)
            }
        })

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: formBody,
        })

        if (!response.ok) {
            console.log(response)

            return Response.json({ errors: "Login failed", success: false })
        }

        const data = await response.json()
        console.log(data)

        return Response.json({ errors: "Login success", success: true })
    }
    catch (error) {
        console.error(error)
    }
}