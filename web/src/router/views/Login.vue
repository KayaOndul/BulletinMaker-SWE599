<template>

    <div>
        <Layout>
            <v-card class="my-4"

                    color="primary"
                    dark
            >
                <div class="d-flex flex-no-wrap justify-space-between ">
                    <v-card-title class="headline">Login</v-card-title>


                </div>

            </v-card>
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
                                v-model="password"
                                :error-messages="passwordErrors"
                                type="password"
                                label="Password"
                                required
                                @input="$v.password.$touch()"
                                @blur="$v.password.$touch()"
                        ></v-text-field>


                        <v-btn class="mr-4 primary" @click="submit">submit</v-btn>
                        <v-btn @click="clear" class="error white--text">close</v-btn>
                    </form>
                </v-card-text>
            </v-card>
        </Layout>
    </div>


</template>
<script>
    import Layout from '../layouts/layout'
    import {validationMixin} from 'vuelidate'
    import {required} from 'vuelidate/lib/validators'
    import {mdiLogin} from '@mdi/js'
    import authService from "../../service/authService";

    export default {
        mixins: [validationMixin],
        components: {Layout},

        validations: {
            password: {required},
            username: {required},

        },

        data: () => ({
            dialog: false,
            password: '',
            username: '',
            svgPath: mdiLogin

        }),

        computed: {

            passwordErrors() {
                const errors = []
                if (!this.$v.password.$dirty) return []
                !this.$v.password.required && errors.push('Password is required.')
                return errors
            },
            usernameErrors() {
                const errors = []
                if (!this.$v.username.$dirty) return []
                !this.$v.username.required && errors.push('Username is required')
                return errors
            },

        },

        methods: {
            submit() {
                this.$v.$touch()
                this.login();
            },
            clear() {
                this.$v.$reset()
                this.password = ''
                this.username = ''
                this.$router.push('/Home')

            },
            login: function () {
                let username = this.username;
                let password = this.password;
                authService.LOGIN({username, password})
                    .then(() => {
                        this.dialog = false
                    })
                    .then(() => {
                        this.$router.push('/')
                    })


                    // eslint-disable-next-line no-console
                    .catch(err => console.log(err))
            }
        },


    }
</script>
