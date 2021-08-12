import models
import views
import controllers


def app():
    app_view1 = views.ShowAddProduct()
    app_view2 = views.ShowProducts()
    app_view3 = views.ShowProduct()
    app_view4 = views.ShowUpdateProduct()
    app_view5 = views.ShowDeleteProduct()
    model = models.Products()
    app_controller1 = controllers.Create(model)
    app_controller2 = controllers.ChangeProduct(model)
    app_controller3 = controllers.DeleteProduct(model)
    app_controller4 = controllers.ReadItems(model)
    app_controller5 = controllers.ReadItem(model)
    app_controller6 = controllers.Exit()

    model.subscribe(app_view1, app_view2, app_view3, app_view4, app_view5)
    app_view6 = views.Start(app_controller1, app_controller2, app_controller3,
                            app_controller4, app_controller5, app_controller6)

    while True:
        app_view6.show_dialog()


if __name__ == '__main__':
    app()
