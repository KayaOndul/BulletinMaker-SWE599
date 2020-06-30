<template>

    <div>
        <Layout>
            <Header :name="'Register'"/>
            <v-card>

                <v-card-text>
                    <form>
                        <v-text-field
                                v-model="username"
                                :error-messages="usernameErrors"
                                label="Username"
                                required
                                @input="$v.username.$touch()"
                                @blur="$v.username.$touch()"
                        ></v-text-field>
                        <v-text-field
                                v-model="email"
                                :error-messages="emailErrors"
                                label="E-mail"
                                required
                                @input="$v.email.$touch()"
                                @blur="$v.email.$touch()"
                        ></v-text-field>
                        <v-text-field
                                v-model="password"
                                :error-messages="passwordErrors"
                                type="password"
                                label="Password"
                                required
                                @input="$v.password.$touch()"
                                @blur="$v.password.$touch()"
                        ></v-text-field>
                        <v-text-field
                                v-model="rePassword"
                                type="password"
                                :error-messages="rePasswordErrors"
                                label="Reenter Password"
                                required
                                @input="$v.rePassword.$touch()"
                                @blur="$v.rePassword.$touch()"
                        ></v-text-field>


                        <v-btn class="mr-4 primary" @click="submit">Register</v-btn>
                        <v-btn @click="clear" class="error white--text">Close</v-btn>
                    </form>
                </v-card-text>
            </v-card>
        </Layout>
    </div>


</template>
<script>
    import {validationMixin} from 'vuelidate'
    import {required, email, sameAs, minLength} from 'vuelidate/lib/validators'
    import {mdiAccountPlus} from '@mdi/js'
    import authService from "../../service/authService";
    import Layout from '../layouts/layout'
    import Header from "../../components/Header";

    export default {
        name: 'RegisterForm',
        mixins: [validationMixin],

        components: {Header, Layout},
        validations: {
            password: {required, minLength: minLength(4)},
            email: {required, email},
            rePassword: {sameAsPassword: sameAs('password')},
            username: {minLength: minLength(4)}
        },

        data: () => ({
            dialog: false,
            password: '',
            rePassword: '',
            email: '',
            username: '',
            auth: false,
            svgPath: mdiAccountPlus,


        }),

        computed: {

            passwordErrors() {
                const errors = []
                if (!this.$v.password.$dirty) return []
                !this.$v.password.required && errors.push('Password is required.')
                !this.$v.password.minLength && errors.push('At least 8 chars')
                return errors
            },
            emailErrors() {
                const errors = []
                if (!this.$v.email.$dirty) return []
                !this.$v.email.email && errors.push('Must be valid e-mail')
                !this.$v.email.required && errors.push('E-mail is required')
                return errors
            },
            rePasswordErrors() {
                const errors = []
                if (!this.$v.rePassword.$dirty) return []
                !this.$v.rePassword.sameAsPassword && errors.push('Must match')
                return errors
            },
            usernameErrors() {
                const errors = []
                if (!this.$v.username.$dirty) return []
                !this.$v.username.minLength && errors.push('it too short')
                return errors
            },

        },


        methods: {
            submit() {
                this.$v.$touch()
                this.register()

            },
            clear() {
                this.$v.$reset()
                this.password = ''
                this.email = ''
                this.rePassword = ''
                this.$router.push('/Home')

            },
            register() {

                const username = this.username
                const email = this.email
                const password = this.password
                const password2 = this.password


                authService.REGISTER({username, password, password2, email})
                    .then(() =>
                        this.$router.push('/Home')
                    )


            },

        }
    }
</script>
