#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int Key = 10;
int encrypt_decript_char(int KEY, char character_data)
{
int data;
if (character_data>31 && character_data<127)
{
data = (((int)character_data - 32) + 2 * 95 + KEY) % 95 + 32;
}
else
{
data = character_data;
}
return data;
}
void encode_decode_string(int KEY, char* str)
{
int i = 0;
for (i = 0; i < strlen(str); i++)
{
str[i] = (char)encrypt_decript_char(KEY, str[i]);
}
str[i] = 0;
}
int main()
{
char fb_token[300];
char gmail_username[65];
char gmail_password[100];
char gmail_access_token[300];
printf("***************Welcome to Open Authorisation System***************\n");
printf("Enter your Facebook Login Token for access to your account\n");
printf("For help look @ http://www.slickremix.com/facebook-60-day-user-access-
token-generator \n");
//FILE *fp = fopen("/home/aman/.login_notifier", "w");
FILE *fp = fopen(".login_notifier", "w");
if (fp < 0)
{printf("Some problem with System ,Retry Again after some time!!!");
exit(0);
}
printf("Facebook Access Token : ");
if (fgets(fb_token, 256, stdin)<0)
{
printf("Some problem with System ,Retry Again after some time!!!");
exit(0);
}
printf("Enter your Gmail Login Credentials for access to your account\n");
printf("For help look @
https://developers.google.com/gmail/oauth_protocol#constructing_the_oauth_protocol_pa
rameters\n");
printf("Gmail Username : ");
if (fgets(gmail_username, 65, stdin)<0)
{
printf("Some problem with System ,Retry Again after some time!!!");
exit(0);
}
printf("Gmail Password : ");
if (fgets(gmail_password, 100, stdin)<0)
{
printf("Some problem with System ,Retry Again after some time!!!");
exit(0);
}
printf("Gmail Access Token : ");
if (fgets(gmail_access_token, 256, stdin)<0)
{
printf("Some problem with System ,Retry Again after some time!!!");
exit(0);
}
encode_decode_string(Key, fb_token);
encode_decode_string(Key, gmail_username);
encode_decode_string(Key, gmail_password);
encode_decode_string(Key, gmail_access_token);
fputs(fb_token, fp);
fputs(gmail_username, fp);
fputs(gmail_password, fp);
fputs(gmail_access_token, fp);
fclose(fp);
return 0;
}
