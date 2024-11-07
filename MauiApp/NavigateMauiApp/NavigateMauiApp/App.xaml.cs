using NavigateMauiApp.Pages;

namespace NavigateMauiApp
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            Home home = new Home();

            NavigationPage navigationPage = new NavigationPage(home);

            MainPage = navigationPage;

        }
    }
}
