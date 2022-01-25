<template>
   <button class="text-white p-1 rounded m-1">
        <p>{{ title }}</p>
    </button>
</template>

<script>
export default {
    props:{
        title:{
            type: String,
            default: "Home",
            required: false
        },
    }
}
</script>