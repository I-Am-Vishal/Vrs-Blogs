var updateBtns=document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId= this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId,'action:',action)
        
    
        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')}
        else{
            updateUserOrder(productId,action)
        }
    
    })
}

function updateUserOrder(productId,action){
    console.log('user is logged in, sending sata..')

    var url = 'http://127.0.0.1:8000/store/update/'

    fetch(url,{
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId,'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:',data)
        location.reload()
    })
}