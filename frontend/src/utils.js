export function showError(message) {
    window.vm.$buefy.notification.open({
        duration: 5000,
        message,
        position: 'is-bottom-right',
        type: 'is-danger',
        hasIcon: true,
        icon: "exclamation-circle",
        "icon-pack": "fas"
    });
}

export function showInfo(message) {
    window.vm.$buefy.notification.open({
        duration: 5000,
        message,
        position: 'is-bottom-right',
        type: 'is-info',
        hasIcon: true,
    });
}


export function catchError(error) {
    const { errors } = error.response.data;
    for (const i in errors) {
        showError(errors[i]);
    }
}
