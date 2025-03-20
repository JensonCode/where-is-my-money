import { Fragment } from 'react/jsx-runtime';
import Nav from '../nav';

export default function AdminLayout({ children, isAdmin }: { children: React.ReactNode, isAdmin: boolean }) {
    if (isAdmin) {
        return (
            <Fragment>
                <Nav />
                {children}
            </Fragment>
        )
    }

    return children
}