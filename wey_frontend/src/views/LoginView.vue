<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2-xl">Войти в аккаунт</h1>
                <p class="mb-6 text-gray-500">
                    Войдите в аккаунт, чтобы пользоваться "наикрутейшей" социальной сетью!
                </p>
                <p class="font-bold">
                    У Вас нет аккаунта? Нажмите <RouterLink :to="{'name': 'signup'}" class="underline">тут,</RouterLink>  чтобы зарегестрироваться!
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label for="">Почта</label><br>
                        <input type="email" placeholder="Ваш почтовый адрес" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">

                    </div>
                    
                    <div>
                        <label for="">Пароль</label><br>
                        <input type="password" placeholder="Придумайте пароль" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Войти</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>