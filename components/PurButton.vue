<template>
   <button class="text-white p-4 rounded m-1 bg-black">
        <a :href="`mailto:eamongreen59@gmail.com?subject=Purchase:%20${piece}`" class="text-2xl"><p>{{ title }}</p></a>
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
        piece:{
            type: String,
            default: "",
            required: false
        },
    }
}
</script>