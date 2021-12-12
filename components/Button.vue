<template>
    <button class="bg-gray-100 text-gray-600 p-1 rounded m-1">
        {{ title }}
    </button>
</template>

<script>
export default {
    props:{
        title:{
            type: String,
            default: "Home",
            required: false
        }
    }
}
</script>