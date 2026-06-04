class CustomSet{
    constructor(){
        this.items=new Map();
    }
    add(element){
        if(this.items.has(element)){
            return false;
        }
        this.items.set(element,element);
        return true;
    }
    has(element){
        return this.items.has(element);
    }
    remove(element){
        return this.items.delete(element);
    }
    size(){
        return this.items.size;
    }
    values(){
        return [...this.items.keys()];
    }
    union(otherSet){
        const unionSet=new CustomSet();
        this.values().forEach(value =>unionSet.add(value));

        otherSet.values().forEach(value => unionSet.add(value));
        return unionSet;
    }
    intersection(otherSet){
        const intersectionSet=new CustomSet();

        const smallerSet=this.size() <otherSet.size()? this:otherSet;
        const largerSet=this.size()<otherSet.size()?otherSet:this;

        smallerSet.values().forEach( value =>{
            if(largerSet.has(value)){
                intersectionSet.add(value);
            }
        });
        return intersectionSet;
    }
}
const setA=new CustomSet();
setA.add(2);
setA.add(4);
setA.add(6);
setA.add(8);
setA.add(10);
const setB=new CustomSet();
setB.add(1);
setB.add(4);
setB.add(7);
setB.add(8);
console.log(setA);
console.log(setB);
setC=setA.union(setB);
console.log(setC);
setD=setA.intersection(setB);
console.log(setD);
setA.remove(2);
console.log(setA);


//----- OUTPUT -------


//--- SET{A} -----
CustomSet {
  items: Map(5) { 2 => 2, 4 => 4, 6 => 6, 8 => 8, 10 => 10 }
}

//---- SET{B} ------
CustomSet { items: Map(4) { 1 => 1, 4 => 4, 7 => 7, 8 => 8 } }

// ---- Union ----
CustomSet {
  items: Map(7) { 2 => 2, 4 => 4, 6 => 6, 8 => 8, 10 => 10, 1 => 1, 7 => 7 }
}

// ---- Intersection ----
CustomSet { items: Map(2) { 4 => 4, 8 => 8 } }

// ---- Remove ------
CustomSet { items: Map(4) { 4 => 4, 6 => 6, 8 => 8, 10 => 10 } }


















