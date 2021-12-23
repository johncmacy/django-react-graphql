import Cookies from "js-cookie";

export default function useCsrfToken() {
  return Cookies.get("csrftoken");
}
