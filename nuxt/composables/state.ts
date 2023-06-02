export const useState = () => {
    const state = reactive({
        url: '',
        apiKey: ''
    })
    const update = (_url: string, _apiKey: string) => {
        state.url = _url
        state.apiKey = _apiKey
        console.log(state)
    }
    return {
        state: readonly(state),
        update
    }
}

export type State = ReturnType<typeof useState>