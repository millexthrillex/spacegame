from datetime import datetime

class TodoItem:
    def __init__(self, description):
        if description == "": 
            raise ValueError("Empty description")

        self.description = description
        self.complete = False

        self.creationDate = datetime.now()


    def save(self):
        return f"{self.complete}|{self.description}"


    def markComplete(self):
        self.complete = True

    def load(toLoad):
        [completion, descr] = toLoad.split('|', 1)
        item = TodoItem(descr)
        item.complete = completion == "True"

        return item

    def __eq__(self, other):
        return self.description == other.description and self.complete == other.complete


if __name__ == "__main__":
  def test_create_TodoItem():
    def doTest(taskDescription):
      item = TodoItem(taskDescription)
  
      assert(item.description == taskDescription)
      assert(item.complete == False)
      assert(item.creationDate)
  
    doTest("Mow lawn")
    doTest("Test 1")
    doTest("Test 2")
    doTest("Test 3")
  
  
  def test_save_TodoItem():
    def doTest(taskDescription):
      item = TodoItem(taskDescription)
  
      result = item.save()
      assert(result == f"False|{taskDescription}")
  
      item.markComplete()
      result = item.save()
      assert(result == f"True|{taskDescription}")
  
    doTest("Mow lawn")
    doTest("Test 1")
    doTest("Test 2")
    doTest("Test 3")
  
  
  def test_task_completion():
    def doTest(taskDescription):
      item = TodoItem(taskDescription)
  
      assert(item.complete == False)
  
      item.markComplete()
  
      assert(item.complete == True)
  
    doTest("Mow lawn")
    doTest("Test 1")
    doTest("Test 2")
    doTest("Test 3")
  
  
  def test_load_todo():
    def doTest(taskDescription):
      item = TodoItem(taskDescription)
  
      loadedItem = TodoItem.load(item.save())
  
      assert(item == loadedItem)
  
      item.markComplete()
  
      loadedItem = TodoItem.load(item.save())
  
      assert(item == loadedItem)
  
    doTest("Mow lawn")
    doTest("Mow|Lawn")
  
  
  def test_empty_todo():
    try:
      TodoItem("")
    except ValueError:
      return
  
    assert(False)
  
  test_create_TodoItem()
  test_save_TodoItem()
  test_task_completion()
  test_load_todo()
  test_empty_todo()
  print("Tests succeeded")

