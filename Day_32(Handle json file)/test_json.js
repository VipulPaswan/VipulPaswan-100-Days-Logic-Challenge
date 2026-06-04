try{
    const data = require('./sample.json');
    // console.log(data);
    console.log(data['name']);
    for(key in data){
        if(typeof data[key]!== 'object'){
            console.log(key,'-',data[key]);
        }
        else if (data[key] instanceof Array){
            const arr = data[key];
            if(typeof arr[0]!== 'object'){
                for(e of arr){
                    console.log(e);
                }
            }

            else{
                for(e of arr){
                    for(k1 in e){
                        console.log(k1,' - ',e[k1]);
                    }
                }
            }
        }
    }
}
catch(error){
    console.log("Error:",error);
}


//----- OUTPUT --------
// KL Rahul
// name - KL Rahul
// age - 32
// is_active - true
// 199
// 50
// 100
// 97
// 85