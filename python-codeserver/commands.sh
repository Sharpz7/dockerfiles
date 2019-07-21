sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sed -i -e "s/ZSH_THEME='robbyrussell'/ZSH_THEME='gnzh'/g" ~/.zshrc