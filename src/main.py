from bson.objectid import ObjectId
import controllers.userController as userController
import controllers.sellerController as sellerController
import controllers.productController as productController
import controllers.purchasesController as purchaseController

# USUÁRIO
userController.findSort()
userController.insert("Vinicius", "337.181.988-43")
userController.findQuery("Vinicius")
userController.update("Vinicius", "Alexandre")
userController.findQuery("Alexandre")
userController.delete("Alexandre")
userController.findSort()

# VENDEDOR
sellerController.findSort()
sellerController.insert("Thiago", "999.999.999-99")
sellerController.findQuery("Thiago")
sellerController.update("Thiago", "Gabriel")
sellerController.findQuery("Gabriel")
sellerController.delete("Gabriel")

# PRODUTO
productController.findSort()
productController.insert("Teclado gamer", "Teclado gamer RGB Mecânico")
productController.findQuery("Teclado gamer")
productController.update("Teclado gamer", "Headset gamer")
productController.findQuery("Headset gamer")
productController.delete("Headset gamer")

# COMPRA
purchaseController.findSort()
purchaseController.insert(ObjectId('624438b0573a957071bb626a'), "Seu Jorge", 350)
purchaseController.update(ObjectId('624438b0573a957071bb626a'), 450)
purchaseController.findQuery(ObjectId('624438b0573a957071bb626a'))
purchaseController.delete(ObjectId('624438b0573a957071bb626a'))