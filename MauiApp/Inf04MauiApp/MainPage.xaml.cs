namespace Inf04MauiApp
{
    public partial class MainPage : ContentPage
    {
     

        public MainPage()
        {
            InitializeComponent();
        }

        private void buttonConfirm_Clicked(object sender, EventArgs e)
        {
            string strEntryMail = entryMail.Text;
            string strEntryPassword = entryPassword.Text;
            string strRepeatPassword = entryRepeatPassword.Text;
            string letter = "@";

            if (!string.IsNullOrEmpty(strEntryMail) && !string.IsNullOrEmpty(strEntryPassword) && !string.IsNullOrEmpty(strRepeatPassword))
            {
                if (!strEntryMail.Contains(letter))
                {

                    showMessage.Text = "Nieprawidłowy adres e-mail";
                }
                if (strEntryPassword != strRepeatPassword)
                {
                    showMessage.Text = "Hasła się różnią";
                }
                if (strEntryMail.Contains(letter) && strEntryPassword == strRepeatPassword)
                    showMessage.Text = "Witaj " + strEntryMail;
            }
            else
                showMessage.Text = "Podano złe dane";
        }
    }

}
