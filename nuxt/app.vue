<template>
  <div>
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
import { useState  } from '~/composables/state'
import StateKey from '~/composables/stateKey'

provide(StateKey, useState())
</script>