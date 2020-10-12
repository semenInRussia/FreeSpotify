import axios from "axios";
import axios_config from "@/vars";

const base_url = `http://localhost:8000`
const url = `${base_url}/api/tracks/top`

function getArtistUrl(artist_name) {
    return url + "/" + artist_name
}

export default {
    state: {
        tracks: [],
        is_loading: false
    },
    getters: {
        tracks(state) {
            return state.tracks;
        },
        loading(state){
            return state.is_loading
        }
    },
    actions: {
        fetchTop(ctx, artist_name ) {
            axios.get(getArtistUrl(artist_name, axios_config))
                 .then(response => {
                     ctx.commit("setLoading", true)
                     let tracks = response.data
                     console.log(tracks)
                     ctx.commit("setTop", tracks)
                 })
                .finally(() => {
                    ctx.commit("setLoading", false)
                })
        }
    },
    mutations: {
        setTop(state, tracks) {
            state.tracks = tracks
        },
        setLoading(state, value) {
            console.log(value)
            state.is_loading = value
        }
    }
}