int lcm(int a, int b){
    int i;
    for(i=a>b?a:b;i<=a*b;i++){
        if(i%a==0 && i%b==0){
            return i;
        }

    return 1;
    }
}

int fact(int n){
    int f=1;
    while(n){
        f=f*n;
        n--;
    }
    return f;
}