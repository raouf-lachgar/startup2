document.addEventListener('DOMContentLoaded',()=>{
    let filter = document.querySelector('.filter_btn');
    let apply = document.querySelector('.apply');
    let container = document.querySelector('.filter')
    filter.addEventListener('click',()=>{
        if (container.style.display=='none')
           container.style.display='block';
        else
           container.style.display='none';
    })
    apply.addEventListener('click',()=>{
           container.style.display='none';
    })
})