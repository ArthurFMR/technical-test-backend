const BASE_URL = "http://localhost:8000";

var app = new Vue({
    el: '#app',
    data: {
        login: true,
        logged: false,
        notification: false,
        notificationMsg: "",
        notes: [],
        userData: {
            username: "",
            password: ""
        },

        noteData: {
            title: "",
            description: ""
        }
    },

    mounted() {
        if (localStorage.getItem("token")) {
            this.logged = true
            this.getNotes()
        } else { this.logged = false }
    },

    methods: {
        changeForm(bool) {
            this.login = bool
        },

        register() {
            let url = `${BASE_URL}/users/register`;

            axios.post(url, this.userData)
                .then(response => {
                    this.login = true;
                    this.userData.username = "";
                    this.userData.password = "";

                    this.setNotification(false, '')

                })
                .catch(err => {
                    let message = err.response.data.error
                    this.setNotification(true, message)
                })
        },

        loginUser() {
            let url = `${BASE_URL}/users/login`;

            axios.post(url, this.userData)
                .then(response => {
                    console.log(response.data.token)
                    localStorage.setItem("token", response.data.token)
                    location.reload()
                })
                .catch(err => {
                    let message = err.response.data.error
                    this.setNotification(true, message)
                })
        },

        addNote() {
            let url = `${BASE_URL}/notes`;
            let token = localStorage.getItem("token");

            axios.post(url, this.noteData, {
                headers: {
                    'Authorization': token
                }
            })
                .then(response => {
                    console.log(response.data)
                    this.notes.push(response.data.note)
                    this.noteData.title = "";
                    this.noteData.description = ""

                    this.setNotification(false, '')
                })
                .catch(err => {
                    let message = err.response.data.error
                    this.setNotification(true, message)
                })
        },

        getNotes() {

            let url = `${BASE_URL}/notes`;
            let token = localStorage.getItem("token");

            axios.get(url, { headers: { 'Authorization': token } })
                .then(response => {
                    this.notes = response.data.notes
                })
                .catch(err => {
                    console.log(err.response.data)
                })
        },

        logout() {
            localStorage.removeItem("token")
            location.reload()
        },

        setNotification(show, msg) {
            this.notificationMsg = msg;
            this.notification = show;
        }

    }
})