import axios, { AxiosInstance, AxiosRequestConfig, AxiosRequestHeaders } from 'axios';

type Response<T> = {
    code: number;
    message: string;
    data: T;
}

type RequestData = {}

class ApiHttp {
    instance: AxiosInstance
    constructor() {
        this.instance = axios.create({
            baseURL: import.meta.env.VITE_SHOP_MANAGEMENT_HOST
        })
        this.instance.interceptors.request.use(
            (values) => {
                const token = localStorage.getItem('http_token')
                if (token !== null && typeof values.headers !== "undefined") {
                  values['headers'].setAuthorization(`token ${token}`)
                }
                return values
            },
            error => {}
        )
        this.instance.interceptors.response.use(
            (response) => {
                if (Object.keys(response.data).includes('code')) {
                    return response.data
                }
                return response.data
            },
            error => {}
        )
    }

    get<T>(url: string, params?: RequestData): Promise<Response<T>> {
        return this.instance.get(url, {params: params})
    }

    post<T>(url: string, data?: RequestData): Promise<Response<T>> {
        return this.instance.post(url, data)
    }

    patch<T>(url: string, data?: RequestData): Promise<Response<T>> {
        return this.instance.patch(url, data)
    }

    put<T>(url: string, data?: RequestData): Promise<Response<T>> {
        return this.instance.put(url, data)
    }

    delete<T>(url: string, data?: RequestData): Promise<Response<T>> {
        return this.instance.delete(url, data)
    }
}

export default ApiHttp;