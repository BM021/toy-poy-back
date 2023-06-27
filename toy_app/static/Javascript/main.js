let mobMenu = document.getElementsByClassName('mob_menu_icon')[0]
mobMenu.addEventListener('click',burgerMenu )
function burgerMenu(){
	document.querySelector('.mob_menu').classList.toggle('hidden')
    document.querySelector('.mob_menu').classList.toggle('active')
}
let catalogBtn= document.querySelector('.catalog_btn')

catalogBtn.addEventListener('click',catalogMenu)

function catalogMenu(){
    document.querySelector('.catalog_menu_mob').classList.toggle('hidden')
    document.querySelector('.catalog_menu_mob').classList.toggle('active')
}