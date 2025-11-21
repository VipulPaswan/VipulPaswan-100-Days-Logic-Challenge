class HashTable {
  constructor(size = 50) {
    this.table = new Array(size);
    this.size = 0;
  }
  _hashFunction(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash += key.charCodeAt(i);
    }
    return hash % this.table.length;
  }
  set(key, value) {
    const index = this._hashFunction(key);
    if (this.table[index] === undefined) {
      this.table[index] = [];
    }
    const chain = this.table[index];
    for (let i = 0; i < chain.length; i++) {
      if (chain[i][0] === key) {
        chain[i][1] = value;
        return;
      }
    }
    chain.push([key, value]);
    this.size++;
  }
  get(key) {
    const index = this._hashFunction(key);
    const chain = this.table[index];

    if (chain) {
      for (let i = 0; i < chain.length; i++) {
        if (chain[i][0] === key) return chain[i][1];
      }
    }
    return undefined;
  }
  remove(key) {
    const index = this._hashFunction(key);
    const chain = this.table[index];

    if (chain) {
      for (let i = 0; i < chain.length; i++) {
        if (chain[i][0] === key) {
          chain.splice(i, 1);
          this.size--;
          return true;
        }
      }
    }
    return false;
  }
  count() {
    return this.size;
  }
}
const ht = new HashTable(10);
ht.set("Vipul", 94);
ht.set("Ashutosh", 92);
ht.set("Sunny", 95);
ht.set("Manu", 91);
ht.set("satendra", 93);

console.log(ht.get("Vipul"));
console.log(ht.get("Ashutosh"));
console.log(ht.get("Sunny"));
console.log(ht.get("Manu"));
console.log(ht.get("satendra"));


//----- OUTPUT --------
94
92
95
91
93



