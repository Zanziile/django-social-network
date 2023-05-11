<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2-xl">Зарегестрироваться</h1>
                <p class="mb-6 text-gray-500">
                    Зарегестрируйте аккаунт, чтобы пользоваться "наикрутейшей" социальной сетью!
                </p>
                <p class="font-bold">
                    У Вас уже есть аккаунт? Нажмите <RouterLink :to="{'name': 'login'}" class="underline">тут,</RouterLink>  чтобы войти через него!
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label for="">Имя и фамилия</label><br>
                        <input type="text" v-model="form.name" placeholder="Укажите Ваше имя и фамилию" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">

                    </div>

                    <div>
                        <label for="">Почта</label><br>
                        <input type="email" v-model="form.email" placeholder="Ваш почтовый адрес" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">

                    </div>
                    
                    <div>
                        <label for="">Пароль</label><br>
                        <input type="password" v-model="form.password1" placeholder="Придумайте пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label for="">Повторите пароль</label><br>
                        <input type="password" v-model="form.password2" placeholder="Повторите пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Зарегестрироваться</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Введите почту')
            }

            if (this.form.name === '') {
                this.errors.push('Введите полное имя')
            }

            if (this.form.password1 === '') {
                this.errors.push('Введите пароль')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('Пароли не совпадают')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Пользователь зарегестрирован. Пожалуйста, авторизуйтесь', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            this.toastStore.showToast(5000, 'Что-то не так. Повторите, пожалуйста попытку', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>