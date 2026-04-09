const userName = document.querySelector(".username")
const userPassword = document.querySelector(".password")
const btnSubmit = document.querySelector(".btn-submit")

const form = document.querySelector(".form-login")

form.addEventListener("submit", async (e) => {
    e.preventDefault()

    try {
        console.log("Intentando login...")

        const res = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                username: userName.value,
                password: userPassword.value
            })
        })

        console.log("STATUS:", res.status)

        const data = await res.json()

        console.log("RESPUESTA:", data)

    } catch (error) {
        console.log("ERROR REAL:", error)
    }
})