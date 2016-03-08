import './ek-select-users.less';
import constants from '../constants';
import Directive from 'directive';
import Controller from './ek-select-users.controller';
import template from './ek-select-users.html';

class SelectUsersDirective extends Directive {
    constructor() {
        super({ Controller, template });

        this.bindToController = {
            selectedUsers: '=',
            placeholder: '@'
        };
    }

    compile(tElement) {
        tElement.addClass('ek-select-users');

        return ($scope) => _.extend($scope, constants);
    }
}

export default SelectUsersDirective;
