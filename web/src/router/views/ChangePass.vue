<template>

    <div>
        <Layout>
            <Header :name="'Change Password'"/>
            <v-card>

                <v-card-text>
                    <form>
                        <v-text-field
                                v-model="password"
                                :error-messages="passwordErrors"
                                type="password"
                                label="New password"
                                required
                                @input="$v.password.$touch()"
                                @blur="$v.password.$touch()"
                        ></v-text-field>
                        <v-text-field
                                v-model="rePassword"
                                type="password"
                                :error-messages="rePasswordErrors"
                                label="Reenter new password"
                                required
                                @input="$v.rePassword.$touch()"
                                @blur="$v.rePassword.$touch()"
                        ></v-text-field>


                        <v-btn class="mr-4 primary" @click="submit">Change Password</v-btn>
                        <v-btn @click="clear" class="error white--text">Close</v-btn>
                    </form>
                </v-card-text>
            </v-card>
        </Layout>
    </div>


</template>
<script>
    import {validationMixin} from 'vuelidate'
    import {required, sameAs, minLength} from 'vuelidate/lib/validators'
    import {mdiAccountPlus} from '@mdi/js'
    import authService from "../../service/authService";
    import Layout from '../layouts/layout'
    import store from "../../store/store";
    import Header from "../../components/Header";

    export default {
        name: 'ChangePassForm',
        mixins: [validationMixin],

        components: {Header, Layout},
        validations: {
            password: {required, minLength: minLength(4)},
            rePassword: {sameAsPassword: sameAs('password')},

        },

        data: () => ({
            dialog: false,
            password: '',
            rePassword: '',
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

            rePasswordErrors() {
                const errors = []
                if (!this.$v.rePassword.$dirty) return []
                !this.$v.rePassword.sameAsPassword && errors.push('Must match')
                return errors
            },


        },


        methods: {
            submit() {
                this.$v.$touch()
                this.changePasssword()

            },
            clear() {
                this.$v.$reset()
                this.password = ''
                this.email = ''
                this.rePassword = ''
                this.$router.push('/Home')

            },
            changePasssword() {

                const username = store.state.auth.username
                const password = this.password
                const password2 = this.password


                authService.CHANGE_PASSWORD({ username,password, password2})
                    .then(() =>
                        this.$router.push('/Home')
                    )


            },

        }
    }
</script>
