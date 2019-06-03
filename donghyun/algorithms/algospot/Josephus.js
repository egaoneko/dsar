const input = [];
let size = 0;
let i = 0;
const rl = require('readline')
.createInterface(process.stdin, {})
.on('line', (line) => {
  if (size === 0) {
    size = parseInt(line, 10);
  } else {   
    input.push(line.split(' ').map(l => parseInt(l, 10)));
    i += 1;
    
    if (i === size) {
      rl.close();
    }
  }
})
.on('close', () => {
  input.forEach(([n, k]) => {
    solve(n, k);
  });
});

function solve(n, k) {
  const list = new LinkedList();

  for (let i = 1; i <= n; i++) {
    const node = new Node(i);
    list.append(node);
  }

  let i = 0;
  let node = list.head.next;
  while(list.length !== 2) {
    if (i !== 0) {
      i -= 1;
      node = node.next;

      if (node === list.tail) {
        node = list.head.next;
      }
      continue;
    }

    i = (k - 1);
    list.delete(node);
    node = node.next;
    if (node === list.tail) {
      node = list.head.next;
    }
  }

  const result = [];
  list.forEach((node) => {
    result.push(node.value);
  })

  console.log(result.join(' '));
}

class LinkedList {
  constructor() {
    this.length = 0;
    this.head = new Node(null);
    this.tail = new Node(null);

    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  append(node) {
    const tail = this.tail;
    const prev = tail.prev;

    prev.next = node;
    node.prev = prev;
    tail.prev = node;
    node.next = tail;
    this.length += 1;
  }

  delete(node) {
    const prev = node.prev;
    const next = node.next;

    prev.next = next;
    next.prev = prev;
    this.length -= 1;
  }

  forEach(callback) {
    if (!callback) {
      return;
    }

    const tail = this.tail;
    let node = this.head;
    while(node.next !== tail) {
      node = node.next;
      callback(node);
    }
  }
}

class Node {
  constructor(value) {
    this.prev = null;
    this.next = null;
    this.value = value;
  }
}