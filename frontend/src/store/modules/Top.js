import axios from "axios";

const base_url = `http://localhost:8000`
const url = `${base_url}/api/tracks/top`

function getArtistUrl(artist_name) {
    return url + "/" + artist_name
}

export default {
    state: {
        tracks: []
    },
    getters: {
        tracks(state) {
            return state.tracks;
        },
    },
    actions: {
        fetchTop(ctx, artist_name ) {
            let tracks;
            axios.get(getArtistUrl(artist_name))
                 .then(response => (tracks = response))

            ctx.commit("setTop", tracks)
        }
    },
    mutations: {
        setTop(state, tracks) {
            state.tracks_top = tracks
        }
    }
}