<template>
    <h1>Indexes</h1>
    <pre>{{ results }}</pre>
</template>

<script setup lang="ts">
import MeiliSearch from 'meilisearch'
import { State } from '~/composables/state';
import StateKey from '~/composables/stateKey'

const { state } = inject(StateKey) as State
const client = new MeiliSearch({ host: state.url, apiKey: state.apiKey })
const index = client.index('news')
const results = ref([])

const searchResults = await index.search('au')
results.value = searchResults.hits as []
</script>