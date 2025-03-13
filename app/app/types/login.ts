import type { components } from "./api"

type LoginFormSchema = components["schemas"]

export type LoginFormData = LoginFormSchema["Body_login_users_login_post"]